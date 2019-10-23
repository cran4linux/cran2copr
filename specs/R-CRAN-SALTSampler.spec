%global packname  SALTSampler
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Efficient Sampling on the Simplex

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-lattice 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
The SALTSampler package facilitates Monte Carlo Markov Chain (MCMC)
sampling of random variables on a simplex. A Self-Adjusting Logit
Transform (SALT) proposal is used so that sampling is still efficient even
in difficult cases, such as those in high dimensions or with parameters
that differ by orders of magnitude. Special care is also taken to maintain
accuracy even when some coordinates approach 0 or 1 numerically.
Diagnostic and graphic functions are included in the package, enabling
easy assessment of the convergence and mixing of the chain within the
constrained space.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
