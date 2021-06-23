%global __brp_check_rpaths %{nil}
%global packname  zGPS.AO
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Zero Inflated Gamma Poisson Shrinker with Adverse Event Ontology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pscl >= 1.5.5
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-hrbrthemes 
BuildRequires:    R-parallel 
Requires:         R-CRAN-pscl >= 1.5.5
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-questionr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-hrbrthemes 
Requires:         R-parallel 

%description
The method zGPS.AO (Zero Inflated Gamma Poisson Shrinker with AE (Adverse
Event) ontology) is based on the zero-inflated negative binomial
distribution. It estimates the association between a specific vaccine and
an adverse event group, as well as associations between that vaccine and
individual adverse events within the adverse event group. This model
handles the adverse event count data with excess zeros and
over-dispersion, and it allows borrowing information from adverse event
data in the same group. Details can be found in "Data Mining in Large
Frequency Tables With Ontology, with an Application to the Vaccine Adverse
Event Reporting System." Bangyao Zhao, Lili Zhao (2020)
<arXiv:2010.12471>.

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
