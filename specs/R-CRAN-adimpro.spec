%global packname  adimpro
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          3%{?dist}
Summary:          Adaptive Smoothing of Digital Images

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ImageMagick
Requires:         dcraw
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-awsMethods >= 1.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-awsMethods >= 1.1.1
Requires:         R-grDevices 
Requires:         R-methods 

%description
Implements tools for manipulation of digital images and the Propagation
Separation approach by Polzehl and Spokoiny (2006)
<DOI:10.1007/s00440-005-0464-1> for smoothing digital images, see Polzehl
and Tabelow (2007) <DOI:10.18637/jss.v019.i01>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/adjust
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
