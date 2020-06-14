%global packname  COMBAT
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          2%{?dist}
Summary:          A Combined Association Test for Genes using Summary Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-corpcor 

%description
Genome-wide association studies (GWAS) have been widely used for
identifying common variants associated with complex diseases. Due to the
small effect sizes of common variants, the power to detect individual risk
variants is generally low. Complementary to SNP-level analysis, a variety
of gene-based association tests have been proposed. However, the power of
existing gene-based tests is often dependent on the underlying genetic
models, and it is not known a priori which test is optimal.  Here we
proposed COMBined Association Test (COMBAT) to incorporate strengths from
multiple existing gene-based tests, including VEGAS, GATES and simpleM.
Compared to individual tests, COMBAT shows higher overall performance and
robustness across a wide range of genetic models. The algorithm behind
this method is described in Wang et al (2017)
<doi:10.1534/genetics.117.300257>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
