%global packname  scalpel
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Processes Calcium Imaging Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-protoclust 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-CRAN-gam 
Requires:         R-Matrix 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-protoclust 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-SDMTools 
Requires:         R-CRAN-gam 

%description
Identifies the locations of neurons, and estimates their calcium
concentrations over time using the SCALPEL method proposed in Petersen,
A., Simon, N., and Witten, D. SCALPEL: Extracting Neurons from Calcium
Imaging Data
<https://ajpetecom.files.wordpress.com/2017/12/scalpel_dec17.pdf>, which
is to appear in the Annals of Applied Statistics.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
