%global __brp_check_rpaths %{nil}
%global packname  sanzo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Color Palettes Based on the Works of Sanzo Wada

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Inspired by the art and color research of Sanzo Wada (1883-1967), his
"Dictionary Of Color Combinations" (2011, ISBN:978-4861522475), and the
interactive site by Dain M. Blodorn Kim
<https://github.com/dblodorn/sanzo-wada>, this package brings Wada's color
combinations to R for easy use in data visualizations. This package honors
60 of Wada's color combinations: 20 duos, 20 trios, and 20 quads.

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
