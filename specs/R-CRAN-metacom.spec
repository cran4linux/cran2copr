%global __brp_check_rpaths %{nil}
%global packname  metacom
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of the 'Elements of Metacommunity Structure'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.2.1
Requires:         R-CRAN-vegan >= 2.2.1

%description
Functions to analyze coherence, boundary clumping, and turnover following
the pattern-based metacommunity analysis of Leibold and Mikkelson 2002
<doi:10.1034/j.1600-0706.2002.970210.x>. The package also includes
functions to visualize ecological networks, and to calculate modularity as
a replacement to boundary clumping.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
