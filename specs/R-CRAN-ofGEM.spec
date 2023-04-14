%global __brp_check_rpaths %{nil}
%global packname  ofGEM
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Meta-Analysis Approach with Filtering for IdentifyingGene-Level Gene-Environment Interactions with GeneticAssociation Data

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-forestplot 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-MASS 
Requires:         R-CRAN-forestplot 

%description
Offers a gene-based meta-analysis test with filtering to detect
gene-environment interactions (GxE) with association data, proposed by
Wang et al. (2018) <doi:10.1002/gepi.22115>. It first conducts a
meta-filtering test to filter out unpromising SNPs by combining all
samples in the consortia data. It then runs a test of
omnibus-filtering-based GxE meta-analysis (ofGEM) that combines the
strengths of the fixed- and random-effects meta-analysis with
meta-filtering. It can also analyze data from multiple ethnic groups.

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
