%global packname  gWidgetstcltk
%global packver   0.0-55.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.55.1
Release:          1%{?dist}
Summary:          Toolkit implementation of gWidgets for tcltk package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-tcltk >= 2.7.0
BuildRequires:    R-CRAN-gWidgets >= 0.0.51
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-digest 
Requires:         R-tcltk >= 2.7.0
Requires:         R-CRAN-gWidgets >= 0.0.51
Requires:         R-methods 
Requires:         R-CRAN-digest 

%description
Port of the gWidgets API to the tcltk package. Requires Tk 8.5 or greater.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/example.tcl
%doc %{rlibdir}/%{packname}/images
%doc %{rlibdir}/%{packname}/pkgIndex.tcl
%doc %{rlibdir}/%{packname}/tcl
%{rlibdir}/%{packname}/tklibs
%{rlibdir}/%{packname}/INDEX
