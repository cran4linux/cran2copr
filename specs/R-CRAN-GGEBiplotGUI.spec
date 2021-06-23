%global __brp_check_rpaths %{nil}
%global packname  GGEBiplotGUI
%global packver   1.0-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive GGE Biplots in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         bwidget
BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-tcltk >= 3.2.2
BuildRequires:    R-CRAN-rgl >= 0.95.1441
BuildRequires:    R-CRAN-tkrplot >= 0.0.23
Requires:         R-tcltk >= 3.2.2
Requires:         R-CRAN-rgl >= 0.95.1441
Requires:         R-CRAN-tkrplot >= 0.0.23

%description
Description: A GUI with which to construct and interact with GGE biplots.

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
%{rlibdir}/%{packname}/INDEX
