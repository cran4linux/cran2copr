%global packname  scan
%global packver   0.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.40
Release:          3%{?dist}%{?buildtag}
Summary:          Single-Case Data Analyses for Single and Multiple BaselineDesigns

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-nlme 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-mblm 
Requires:         R-stats 
Requires:         R-nlme 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-car 
Requires:         R-MASS 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-mblm 

%description
A collection of procedures for analysing, visualising, and managing
single-case data. These include piecewise linear regression models,
multilevel models, overlap indices (PND, PEM, PAND, PET, tauU, baseline
corrected tau), and randomization tests. Data preparation functions
support outlier detection, handling missing values, scaling, truncating,
rank transformation, and smoothing. An exporting function help to generate
html and latex tables in a publication friendly style. More details can be
found at <https://jazznbass.github.io/scan-Book/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
