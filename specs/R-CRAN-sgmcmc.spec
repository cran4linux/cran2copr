%global __brp_check_rpaths %{nil}
%global packname  sgmcmc
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Gradient Markov Chain Monte Carlo

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-tensorflow 
Requires:         R-utils 
Requires:         R-CRAN-reticulate 

%description
Provides functions that performs popular stochastic gradient Markov chain
Monte Carlo (SGMCMC) methods on user specified models. The required
gradients are automatically calculated using 'TensorFlow'
<https://www.tensorflow.org/>, an efficient library for numerical
computation. This means only the log likelihood and log prior functions
need to be specified. The methods implemented include stochastic gradient
Langevin dynamics (SGLD), stochastic gradient Hamiltonian Monte Carlo
(SGHMC), stochastic gradient Nose-Hoover thermostat (SGNHT) and their
respective control variate versions for increased efficiency. References:
M. Welling, Y. W. Teh (2011)
<http://www.icml-2011.org/papers/398_icmlpaper.pdf>; T. Chen, E. B. Fox,
C. E. Guestrin (2014) <arXiv:1402.4102>; N. Ding, Y. Fang, R. Babbush, C.
Chen, R. D. Skeel, H. Neven (2014)
<https://papers.nips.cc/paper/5592-bayesian-sampling-using-stochastic-gradient-thermostats>;
J. Baker, P. Fearnhead, E. B. Fox, C. Nemeth (2017) <arXiv:1706.05439>.
For more details see <doi:10.18637/jss.v091.i03>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
