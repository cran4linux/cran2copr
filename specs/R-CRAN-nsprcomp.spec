%global __brp_check_rpaths %{nil}
%global packname  nsprcomp
%global packver   0.5.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Negative and Sparse PCA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Two methods for performing a constrained principal component analysis
(PCA), where non-negativity and/or sparsity constraints are enforced on
the principal axes (PAs). The function 'nsprcomp' computes one principal
component (PC) after the other. Each PA is optimized such that the
corresponding PC has maximum additional variance not explained by the
previous components. In contrast, the function 'nscumcomp' jointly
computes all PCs such that the cumulative variance is maximal. Both
functions have the same interface as the 'prcomp' function from the
'stats' package (plus some extra parameters), and both return the result
of the analysis as an object of class 'nsprcomp', which inherits from
'prcomp'. See
<https://sigg-iten.ch/learningbits/2013/05/27/nsprcomp-is-on-cran/> and
Sigg et al. (2008) <doi:10.1145/1390156.1390277> for more details.

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
