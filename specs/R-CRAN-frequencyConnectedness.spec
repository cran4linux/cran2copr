%global packname  frequencyConnectedness
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Spectral Decomposition of Connectedness Measures

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-methods 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-pbapply 
Requires:         R-methods 

%description
Accompanies a paper (Barunik, Krehlik (2018) <doi:10.1093/jjfinec/nby001>)
dedicated to spectral decomposition of connectedness measures and their
interpretation. We implement all the developed estimators as well as the
historical counterparts. For more information, see the help or GitHub page
(<https://github.com/tomaskrehlik/frequencyConnectedness>) for relevant
information.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
