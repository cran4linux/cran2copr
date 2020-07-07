%global packname  RcmdrPlugin.sos
%global packver   0.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}
Summary:          Efficiently search the R help pages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.0.1
BuildRequires:    R-CRAN-tcltk2 >= 1.2.7
BuildRequires:    R-CRAN-sos >= 1.2.3
BuildRequires:    R-tcltk 
Requires:         R-CRAN-Rcmdr >= 2.0.1
Requires:         R-CRAN-tcltk2 >= 1.2.7
Requires:         R-CRAN-sos >= 1.2.3
Requires:         R-tcltk 

%description
Rcmdr interface to the 'sos' package. The plug-in renders the 'sos'
searching functionality easily accessible via the Rcmdr menus. It also
simplifies the task of performing multiple searches and subsequently
obtaining the union or the intersection of the results.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

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
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/LIMITATIONS
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
