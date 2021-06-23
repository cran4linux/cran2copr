%global __brp_check_rpaths %{nil}
%global packname  fscaret
%global packver   0.9.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          Automated Feature Selection from 'caret'

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-hmeasure 
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-hmeasure 
Requires:         R-utils 
Requires:         R-parallel 

%description
Automated feature selection using variety of models provided by 'caret'
package. This work was funded by Poland-Singapore bilateral cooperation
project no 2/3/POL-SIN/2012.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
