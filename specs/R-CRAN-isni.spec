%global packname  isni
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Index of Local Sensitivity to Nonignorability

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-mixor 
BuildRequires:    R-CRAN-lme4 
Requires:         R-nlme 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-mixor 
Requires:         R-CRAN-lme4 

%description
The current version provides functions to compute, print and summarize the
Index of Sensitivity to Nonignorability (ISNI) in the generalized linear
model for independent data, and in the marginal multivariate Gaussian
model and the mixed-effects models for continuous and binary
longitudinal/clustered data. It allows for arbitrary patterns of
missingness in the regression outcomes caused by dropout and/or
intermittent missingness. One can compute the sensitivity index without
estimating any nonignorable models or positing specific magnitude of
nonignorability. Thus ISNI provides a simple quantitative assessment of
how robust the standard estimates assuming missing at random is with
respect to the assumption of ignorability. For a tutorial, download at
<http://huixie.people.uic.edu/Research/ISNI_R_tutorial.pdf>. For more
details, see Troxel Ma and Heitjan (2004) and Xie and Heitjan (2004)
<doi:10.1191/1740774504cn005oa> and Ma Troxel and Heitjan (2005)
<doi:10.1002/sim.2107> and Xie (2008) <doi:10.1002/sim.3117> and Xie
(2012) <doi:10.1016/j.csda.2010.11.021> and Xie and Qian (2012)
<doi:10.1002/jae.1157>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
