%global __brp_check_rpaths %{nil}
%global packname  MANOVA.RM
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Resampling-Based Analysis of Multivariate Data and Repeated Measures Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51
BuildRequires:    R-CRAN-plotrix >= 3.5.12
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magic >= 1.5.9
BuildRequires:    R-CRAN-Matrix >= 1.2.17
BuildRequires:    R-CRAN-data.table >= 1.12.6
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-MASS >= 7.3.51
Requires:         R-CRAN-plotrix >= 3.5.12
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magic >= 1.5.9
Requires:         R-CRAN-Matrix >= 1.2.17
Requires:         R-CRAN-data.table >= 1.12.6
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-multcomp 

%description
Implemented are various tests for semi-parametric repeated measures and
general MANOVA designs that do neither assume multivariate normality nor
covariance homogeneity, i.e., the procedures are applicable for a wide
range of general multivariate factorial designs. In addition to asymptotic
inference methods, novel bootstrap and permutation approaches are
implemented as well. These provide more accurate results in case of small
to moderate sample sizes. Furthermore, post-hoc comparisons are provided
for the multivariate analyses. Friedrich, S., Konietschke, F. and Pauly,
M. (2019) <doi:10.32614/RJ-2019-051>.

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
