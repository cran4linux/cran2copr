%global __brp_check_rpaths %{nil}
%global packname  mixdir
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Cluster High Dimensional Categorical Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-Rcpp 

%description
Scalable Bayesian clustering of categorical datasets. The package
implements a hierarchical Dirichlet (Process) mixture of multinomial
distributions. It is thus a probabilistic latent class model (LCM) and can
be used to reduce the dimensionality of hierarchical data and cluster
individuals into latent classes. It can automatically infer an appropriate
number of latent classes or find k classes, as defined by the user.  The
model is based on a paper by Dunson and Xing (2009)
<doi:10.1198/jasa.2009.tm08439>, but implements a scalable variational
inference algorithm so that it is applicable to large datasets. It is
described and tested in the accompanying paper by Ahlmann-Eltze and Yau
(2018) <doi:10.1109/DSAA.2018.00068>.

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
