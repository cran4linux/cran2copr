%global packname  basket
%global packver   0.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.1
Release:          1%{?dist}
Summary:          Basket Trial Analysis

License:          LGPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-rlang 

%description
Implementation of multisource exchangeability models for Bayesian analyses
of prespecified subgroups arising in the context of basket trial design
and monitoring.  The R 'basket' package facilitates implementation of the
binary, symmetric multi-source exchangeability model (MEM) with posterior
inference arising from both exact computation and Markov chain Monte Carlo
sampling. Analysis output includes full posterior samples as well as
posterior probabilities, highest posterior density (HPD) interval
boundaries, effective sample sizes (ESS), mean and median estimations,
posterior exchangeability probability matrices, and maximum a posteriori
MEMs. In addition to providing "basketwise" analyses, the package includes
similar calculations for "clusterwise" analyses for which subgroups are
combined into meta-baskets, or clusters, using graphical clustering
algorithms that treat the posterior exchangeability probabilities as edge
weights. In addition plotting tools are provided to visualize basket and
cluster densities as well as their exchangeability.  References include
Hyman, D.M., Puzanov, I., Subbiah, V., Faris, J.E., Chau, I., Blay, J.Y.,
Wolf, J., Raje, N.S., Diamond, E.L., Hollebecque, A. and Gervais, R (2015)
<doi:10.1056/NEJMoa1502309>; Hobbs, B.P. and Landin, R. (2018)
<doi:10.1002/sim.7893>; Hobbs, B.P., Kane, M.J., Hong, D.S. and Landin, R.
(2018) <doi:10.1093/annonc/mdy457>; and Kaizer, A.M., Koopmeiners, J.S.
and Hobbs, B.P. (2017) <doi:10.1093/biostatistics/kxx031>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
