%global __brp_check_rpaths %{nil}
%global packname  InterVA4
%global packver   1.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.6
Release:          3%{?dist}%{?buildtag}
Summary:          Replicate and Analyse 'InterVA4'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides an R version of the 'InterVA4' software
(<http://www.interva.net>) for coding cause of death from verbal
autopsies. It also provides simple graphical representation of individual
and population level statistics.

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
