%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iPRISM
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Intelligent Predicting Response to Cancer Immunotherapy Through Systematic Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 

%description
Immunotherapy has revolutionized cancer treatment, but predicting patient
response remains challenging. Here, we presented Intelligent Predicting
Response to cancer Immunotherapy through Systematic Modeling (iPRISM), a
novel network-based model that integrates multiple data types to predict
immunotherapy outcomes. It incorporates gene expression, biological
functional network, tumor microenvironment characteristics, immune-related
pathways, and clinical data to provide a comprehensive view of factors
influencing immunotherapy efficacy. By identifying key genetic and
immunological factors, it provides an insight for more personalized
treatment strategies and combination therapies to overcome resistance
mechanisms.

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
