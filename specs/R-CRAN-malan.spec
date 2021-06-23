%global __brp_check_rpaths %{nil}
%global packname  malan
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}%{?buildtag}
Summary:          MAle Lineage ANalysis

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-tidygraph >= 1.0.0.9999
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.880.1.0
BuildRequires:    R-CRAN-dplyr >= 0.7.3
BuildRequires:    R-CRAN-RcppProgress >= 0.2.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.7
BuildRequires:    R-methods 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-tidygraph >= 1.0.0.9999
Requires:         R-CRAN-RcppArmadillo >= 0.9.880.1.0
Requires:         R-CRAN-dplyr >= 0.7.3
Requires:         R-CRAN-RcppProgress >= 0.2.1
Requires:         R-CRAN-Rcpp >= 0.12.7
Requires:         R-methods 

%description
MAle Lineage ANalysis by simulating genealogies backwards and imposing
short tandem repeats (STR) mutations forwards. Intended for forensic Y
chromosomal STR (Y-STR) haplotype analyses. Numerous analyses are
possible, e.g. number of matches and meiotic distance to matches. Refer to
papers mentioned in citation("malan") (DOI's:
<doi:10.1371/journal.pgen.1007028>, <doi:10.21105/joss.00684> and
<doi:10.1016/j.fsigen.2018.10.004>).

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
