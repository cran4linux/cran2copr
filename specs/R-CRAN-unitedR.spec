%global __brp_check_rpaths %{nil}
%global packname  unitedR
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          2%{?dist}%{?buildtag}
Summary:          Assessment and Evaluation of Formations in United

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
Requires:         R-methods 
Requires:         R-CRAN-plyr 

%description
United is a software tool which can be downloaded at the following website
<http://www.schroepl.net/pbm/software/united/>. In general, it is a
virtual manager game for football teams. This package contains helpful
functions for determining an optimal formation for a virtual match in
United. E.g. knowing that the opponent has a strong defensive it is
advisable to beat him in the midfield. Furthermore, this package contains
functions for computing the optimal usage of hardness in a game.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
