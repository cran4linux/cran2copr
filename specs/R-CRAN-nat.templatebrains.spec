%global packname  nat.templatebrains
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          2%{?dist}
Summary:          NeuroAnatomy Toolbox ('nat') Extension for Handling TemplateBrains

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-nat >= 1.8.6
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-nat >= 1.8.6
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-memoise 

%description
Extends package 'nat' (NeuroAnatomy Toolbox) by providing objects and
functions for handling template brains.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
