%global packname  BOIN
%global packver   2.6.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.9
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Optimal INterval (BOIN) Design for Single-Agent andDrug- Combination Phase I Clinical Trials

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
Requires:         R-CRAN-Iso 

%description
The Bayesian optimal interval (BOIN) design is a novel phase I clinical
trial design for finding the maximum tolerated dose (MTD). It can be used
to design both single-agent and drug-combination trials. The BOIN design
is motivated by the top priority and concern of clinicians when testing a
new drug, which is to effectively treat patients and minimize the chance
of exposing them to subtherapeutic or overly toxic doses. The prominent
advantage of the BOIN design is that it achieves simplicity and superior
performance at the same time. The BOIN design is algorithm-based and can
be implemented in a simple way similar to the traditional 3+3 design. The
BOIN design yields an average performance that is comparable to that of
the continual reassessment method (CRM, one of the best model-based
designs) in terms of selecting the MTD, but has a substantially lower risk
of assigning patients to subtherapeutic or overly toxic doses. For
tutorial, please check Yan et al. (2020) <doi:10.18637/jss.v094.i13>.

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
