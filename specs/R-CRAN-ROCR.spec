%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROCR
%global packver   1.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing the Performance of Scoring Classifiers

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gplots 
Requires:         R-stats 

%description
ROC graphs, sensitivity/specificity curves, lift charts, and
precision/recall plots are popular examples of trade-off visualizations
for specific pairs of performance measures. ROCR is a flexible tool for
creating cutoff-parameterized 2D performance curves by freely combining
two from over 25 performance measures (new performance measures can be
added using a standard interface). Curves from different cross-validation
or bootstrapping runs can be averaged by different methods, and standard
deviations, standard errors or box plots can be used to visualize the
variability across the runs. The parameterization can be visualized by
printing cutoff values at the corresponding curve positions, or by
coloring the curve according to cutoff. All components of a performance
plot can be quickly adjusted using a flexible parameter dispatching
mechanism. Despite its flexibility, ROCR is easy to use, with only three
commands and reasonable default values for all optional parameters.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
