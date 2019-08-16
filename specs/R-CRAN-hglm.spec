%global packname  hglm
%global packver   2.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}
Summary:          Hierarchical Generalized Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-hglm.data 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-hglm.data 

%description
Implemented here are procedures for fitting hierarchical generalized
linear models (HGLM). It can be used for linear mixed models and
generalized linear mixed models with random effects for a variety of links
and a variety of distributions for both the outcomes and the random
effects. Fixed effects can also be fitted in the dispersion part of the
mean model. As statistical models, HGLMs were initially developed by Lee
and Nelder (1996) <https://www.jstor.org/stable/2346105?seq=1>. We provide
an implementation (Ronnegard, Alam and Shen 2010)
<https://journal.r-project.org/archive/2010-2/RJournal_2010-2_Roennegaard~et~al.pdf>
following Lee, Nelder and Pawitan (2006) <ISBN: 9781420011340> with
algorithms extended for spatial modeling (Alam, Ronnegard and Shen 2015)
<https://journal.r-project.org/archive/2015/RJ-2015-017/RJ-2015-017.pdf>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
