%global __brp_check_rpaths %{nil}
%global packname  stochprofML
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Profiling using Maximum Likelihood Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 

%description
New Version of the R package originally accompanying the paper
"Parameterizing cell-to-cell regulatory heterogeneities via stochastic
transcriptional profiles" by Sameer S Bajikar, Christiane Fuchs, Andreas
Roller, Fabian J Theis and Kevin A Janes (PNAS 2014, 111(5), E626-635
<doi:10.1073/pnas.1311647111>). In this paper, we measure expression
profiles from small heterogeneous populations of cells, where each cell is
assumed to be from a mixture of lognormal distributions. We perform
maximum likelihood estimation in order to infer the mixture ratio and the
parameters of these lognormal distributions from the cumulated expression
measurements. The main difference of this new package version to the
previous one is that it is now possible to use different n's, i.e. a
dataset where each tissue sample originates from a different number of
cells. We used this on pheno-seq data, see: Tirier, S.M., Park, J.,
Preusser, F. et al. Pheno-seq - linking visual features and gene
expression in 3D cell culture systems. Sci Rep 9, 12367 (2019)
<doi:10.1038/s41598-019-48771-4>).

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
%{rlibdir}/%{packname}/INDEX
