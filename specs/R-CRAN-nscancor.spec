%global __brp_check_rpaths %{nil}
%global packname  nscancor
%global packver   0.6.1-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1.25
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Negative and Sparse CCA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Two implementations of canonical correlation analysis (CCA) that are based
on iterated regression. By choosing the appropriate regression algorithm
for each data domain, it is possible to enforce sparsity, non-negativity
or other kinds of constraints on the projection vectors. Multiple
canonical variables are computed sequentially using a generalized
deflation scheme, where the additional correlation not explained by
previous variables is maximized. 'nscancor' is used to analyze paired data
from two domains, and has the same interface as the 'cancor' function from
the 'stats' package (plus some extra parameters). 'mcancor' is appropriate
for analyzing data from three or more domains. See
<http://sigg-iten.ch/learningbits/2014/01/20/canonical-correlation-analysis-under-constraints/>
and Sigg et al. (2007) <doi:10.1109/MLSP.2007.4414315> for more details.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/atexample
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
