%global __brp_check_rpaths %{nil}
%global packname  ggjoy
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Joyplots in 'ggplot2'

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggridges >= 0.4.0
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges >= 0.4.0
Requires:         R-CRAN-ggplot2 

%description
Joyplots provide a convenient way of visualizing changes in distributions
over time or space. This package enables the creation of such plots in
'ggplot2'.

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
