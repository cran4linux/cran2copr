%global __brp_check_rpaths %{nil}
%global packname  directotree
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Creates an Interactive Tree Structure of a Directory

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.tree >= 0.7.6
BuildRequires:    R-CRAN-collapsibleTree >= 0.1.6
Requires:         R-CRAN-data.tree >= 0.7.6
Requires:         R-CRAN-collapsibleTree >= 0.1.6

%description
Represents the content of a directory as an interactive collapsible tree.
Offers the possibility to assign a text (e.g., a 'Readme.txt') to each
folder (represented as a clickable node), so that when the user hovers the
pointer over a node, the corresponding text is displayed as a tooltip.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
