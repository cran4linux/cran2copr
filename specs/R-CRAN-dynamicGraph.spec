%global packname  dynamicGraph
%global packver   0.2.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2.6
Release:          1%{?dist}
Summary:          dynamicGraph

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.1
Requires:         R-core >= 1.8.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggm 
BuildRequires:    R-tcltk 
Requires:         R-methods 
Requires:         R-CRAN-ggm 
Requires:         R-tcltk 

%description
Interactive graphical tool for manipulating graphs

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
%doc %{rlibdir}/%{packname}/demo.source
%doc %{rlibdir}/%{packname}/old.demos
%{rlibdir}/%{packname}/INDEX
