%global __brp_check_rpaths %{nil}
%global packname  DOS2
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          Design of Observational Studies, Companion to the Second Edition

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sensitivity2x2xk 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sensitivitymult 
BuildRequires:    R-CRAN-sensitivitymv 
BuildRequires:    R-CRAN-senstrat 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-sensitivity2x2xk 
Requires:         R-graphics 
Requires:         R-CRAN-sensitivitymult 
Requires:         R-CRAN-sensitivitymv 
Requires:         R-CRAN-senstrat 

%description
Contains data sets, examples and software from the Second Edition of
"Design of Observational Studies"; see Rosenbaum, P.R. (2010)
<doi:10.1007/978-1-4419-1213-8>.

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
