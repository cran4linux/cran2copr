%global packname  PBSadmb
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}
Summary:          ADMB for R Using Scripts or GUI

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-PBSmodelling >= 2.68.6
BuildRequires:    R-methods 
Requires:         R-CRAN-PBSmodelling >= 2.68.6
Requires:         R-methods 

%description
A collection of software provides R support for 'ADMB' (Automatic
Differentiation Model Builder) and a 'GUI' interface facilitates the
conversion of 'ADMB' template code to 'C code' followed by compilation to
a binary executable. Stand-alone functions can also be run by users not
interested in clicking a 'GUI'.

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
%doc %{rlibdir}/%{packname}/ADMtools
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/win
%{rlibdir}/%{packname}/INDEX
