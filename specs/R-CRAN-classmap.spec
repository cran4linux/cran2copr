%global packname  classmap
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Classification Results by Classmaps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-gridExtra 

%description
Tools to visualize the results of a classification obtained by
discriminant analysis, k-nearest neighbors, and support vector machines,
for two or more classes. Implements the techniques described and
illustrated in Raymaekers, Rousseeuw and Hubert (2021), Class maps for
visualizing classification results, Technometrics, to appear. In addition
to class maps, also stacked plots are made. Examples can be found in the
vignettes: "Discriminant_analysis_examples","K_nearest_neighbors_examples"
and "Support_vector_machine_examples".

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
