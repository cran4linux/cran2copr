%global __brp_check_rpaths %{nil}
%global packname  tmvmixnorm
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sampling from Truncated Multivariate Normal and t Distributions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-MASS 

%description
Efficient sampling of truncated multivariate (scale) mixtures of normals
under linear inequality constraints is nontrivial due to the analytically
intractable normalizing constant. Meanwhile, traditional methods may
subject to numerical issues, especially when the dimension is high and
dependence is strong.  Algorithms proposed by Li and Ghosh (2015) <doi:
10.1080/15598608.2014.996690> are adopted for overcoming difficulties in
simulating truncated distributions. Efficient rejection sampling for
simulating truncated univariate normal distribution is included in the
package, which shows superiority in terms of acceptance rate and numerical
stability compared to existing methods and R packages. An efficient
function for sampling from truncated multivariate normal distribution
subject to convex polytope restriction regions based on Gibbs sampler for
conditional truncated univariate distribution is provided. By extending
the sampling method, a function for sampling truncated multivariate
Student's t distribution is also developed.  Moreover, the proposed method
and computation remain valid for high dimensional and strong dependence
scenarios. Empirical results in Li and Ghosh (2015) <doi:
10.1080/15598608.2014.996690> illustrated the superior performance in
terms of various criteria (e.g. mixing and integrated auto-correlation
time).

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
