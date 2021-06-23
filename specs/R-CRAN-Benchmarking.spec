%global __brp_check_rpaths %{nil}
%global packname  Benchmarking
%global packver   0.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29
Release:          1%{?dist}%{?buildtag}
Summary:          Benchmark and Frontier Analysis Using DEA and SFA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-quadprog 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 

%description
Methods for frontier analysis, Data Envelopment Analysis (DEA), under
different technology assumptions (fdh, vrs, drs, crs, irs, add/frh, and
fdh+), and using different efficiency measures (input based, output based,
hyperbolic graph, additive, super, and directional efficiency). Peers and
slacks are available, partial price information can be included, and
optimal cost, revenue and profit can be calculated. Evaluation of mergers
is also supported.  Methods for graphing the technology sets are also
included. There is also support for comparative methods based on
Stochastic Frontier Analyses (SFA) and for convex nonparametric least
squares for convex functions (StoNED). In general, the methods can be used
to solve not only standard models, but also many other model variants. It
complements the book, Bogetoft and Otto, Benchmarking with DEA, SFA, and
R, Springer-Verlag, 2011, but can of course also be used as a stand-alone
package.

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
