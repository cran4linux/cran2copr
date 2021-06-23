%global __brp_check_rpaths %{nil}
%global packname  inflection
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          Finds the Inflection Point of a Curve

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Implementation of methods Extremum Surface Estimator (ESE) and Extremum
Distance Estimator (EDE) to identify the inflection point of a curve .
Christopoulos, DT (2014) <arXiv:1206.5478v2 [math.NA]> . Christopoulos, DT
(2016)
<https://veltech.edu.in/wp-content/uploads/2016/04/Paper-04-2016.pdf> .
Christopoulos, DT (2016) <doi:10.2139/ssrn.3043076> .

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
