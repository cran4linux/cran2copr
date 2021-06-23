%global __brp_check_rpaths %{nil}
%global packname  epiDisplay
%global packver   3.5.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Epidemiological Data Display Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.2
Requires:         R-core >= 2.6.2
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
Requires:         R-foreign 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-nnet 

%description
Package for data exploration and result presentation. Full 'epicalc'
package with data management functions is available at
'<http://medipe.psu.ac.th/epicalc>'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
