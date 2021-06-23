%global __brp_check_rpaths %{nil}
%global packname  TreeSearch
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Phylogenetic Tree Search Using Custom Optimality Criteria

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-phangorn >= 2.2.1
BuildRequires:    R-CRAN-TreeTools >= 1.0.0
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-phangorn >= 2.2.1
Requires:         R-CRAN-TreeTools >= 1.0.0
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Searches for phylogenetic trees that are optimal using a user-defined
criterion. Handles inapplicable data using the algorithm of Brazeau,
Guillerme and Smith (2019) <doi:10.1093/sysbio/syy083>. Implements Profile
Parsimony (Faith and Trueman, 2001) <doi:10.1080/10635150118627>, and
Successive Approximations (Farris, 1969) <doi:10.2307/2412182>.

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
