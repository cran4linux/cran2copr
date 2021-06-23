%global __brp_check_rpaths %{nil}
%global packname  MAclinical
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Class prediction based on microarray data and clinicalparameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.1
Requires:         R-core >= 2.4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-plsgenomics 
BuildRequires:    R-CRAN-st 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-party 
Requires:         R-CRAN-plsgenomics 
Requires:         R-CRAN-st 
Requires:         R-CRAN-e1071 

%description
'Maclinical' implements class prediction using both microarray data and
clinical parameters. It addresses the question of the additional
predictive value of microarray data. Class prediction is performed using a
two-step method combining (pre-validated) PLS dimension reduction and
random forests.

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
%{rlibdir}/%{packname}/INDEX
