%global packname  tfio
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          2%{?dist}
Summary:          Interface to 'TensorFlow IO'

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow >= 1.9
BuildRequires:    R-CRAN-tfdatasets >= 1.9
BuildRequires:    R-CRAN-reticulate >= 1.10
BuildRequires:    R-CRAN-forge 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-tensorflow >= 1.9
Requires:         R-CRAN-tfdatasets >= 1.9
Requires:         R-CRAN-reticulate >= 1.10
Requires:         R-CRAN-forge 
Requires:         R-CRAN-magrittr 

%description
Interface to 'TensorFlow IO', Datasets and filesystem extensions
maintained by `TensorFlow SIG-IO`
<https://github.com/tensorflow/community/blob/master/sigs/io/CHARTER.md>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
