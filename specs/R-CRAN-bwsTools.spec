%global packname  bwsTools
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Case 1 Best-Worst Scaling (MaxDiff) Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-crossdes 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-crossdes 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Tools to design best-worst scaling designs (i.e., balanced incomplete
block designs) and to analyze data from these designs, using aggregate and
individual methods such as: difference scores, Louviere, Lings, Islam,
Gudergan, & Flynn (2013) <doi:10.1016/j.ijresmar.2012.10.002>; analytical
estimation, Lipovetsky & Conklin (2014) <doi:10.1016/j.jocm.2014.02.001>;
empirical Bayes, Lipovetsky & Conklin (2015)
<doi:10.1142/S1793536915500028>; Elo, Hollis (2018)
<doi:10.3758/s13428-017-0898-2>; and network-based measures.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
