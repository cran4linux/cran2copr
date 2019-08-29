%global packname  LVGP
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}
Summary:          Latent Variable Gaussian Process Modeling with Qualitative andQuantitative Input Variables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.5
BuildRequires:    R-parallel >= 3.2.5
BuildRequires:    R-CRAN-randtoolbox >= 1.17
BuildRequires:    R-CRAN-lhs >= 0.14
Requires:         R-stats >= 3.2.5
Requires:         R-parallel >= 3.2.5
Requires:         R-CRAN-randtoolbox >= 1.17
Requires:         R-CRAN-lhs >= 0.14

%description
Fit response surfaces for datasets with latent-variable Gaussian process
modeling, predict responses for new inputs, and plot latent variables
locations in the latent space (only 1D or 2D). The input variables of the
datasets can be quantitative, qualitative/categorical or mixed. The output
variable of the datasets is a scalar (quantitative). The optimization of
the likelihood function is done using a successive
approximation/relaxation algorithm similar to another GP modeling package
"GPM". The modeling method is published in "A Latent Variable Approach to
Gaussian Process Modeling with Qualitative and Quantitative Factors" by
Yichi Zhang, Siyu Tao, Wei Chen, and Daniel W. Apley (2018)
<arXiv:1806.07504>. The package is developed in IDEAL of Northwestern
University.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
