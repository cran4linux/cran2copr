%global __brp_check_rpaths %{nil}
%global packname  SRCS
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Ranking Color Scheme for Multiple PairwiseComparisons

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Implementation of the SRCS method for a color-based visualization of the
results of multiple pairwise tests on a large number of problem
configurations, proposed in: I.G. del Amo, D.A. Pelta. SRCS: a technique
for comparing multiple algorithms under several factors in dynamic
optimization problems. In: E. Alba, A. Nakib, P. Siarry (Eds.),
Metaheuristics for Dynamic Optimization. Series: Studies in Computational
Intelligence 433, Springer, Berlin/Heidelberg, 2012.

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
