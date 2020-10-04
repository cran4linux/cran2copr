%global packname  subspace
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to OpenSubspace

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.0.0
BuildRequires:    R-CRAN-colorspace >= 1.0
BuildRequires:    R-CRAN-rJava >= 0.9
BuildRequires:    R-CRAN-ggvis >= 0.4.2
Requires:         R-CRAN-stringr >= 1.0.0
Requires:         R-CRAN-colorspace >= 1.0
Requires:         R-CRAN-rJava >= 0.9
Requires:         R-CRAN-ggvis >= 0.4.2

%description
An interface to 'OpenSubspace', an open source framework for evaluation
and exploration of subspace clustering algorithms in WEKA (see
<http://dme.rwth-aachen.de/de/opensubspace> for more information).  Also
performs visualization.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
