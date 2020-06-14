%global packname  stabs
%global packver   0.6-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          2%{?dist}
Summary:          Stability Selection with Error Control

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Resampling procedures to assess the stability of selected variables with
additional finite sample error control for high-dimensional variable
selection procedures such as Lasso or boosting. Both, standard stability
selection (Meinshausen & Buhlmann, 2010,
<doi:10.1111/j.1467-9868.2010.00740.x>) and complementary pairs stability
selection with improved error bounds (Shah & Samworth, 2013,
<doi:10.1111/j.1467-9868.2011.01034.x>) are implemented. The package can
be combined with arbitrary user specified variable selection approaches.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
