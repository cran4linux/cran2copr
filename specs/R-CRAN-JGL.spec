%global __brp_check_rpaths %{nil}
%global packname  JGL
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Performs the Joint Graphical Lasso for Sparse Inverse CovarianceEstimation on Multiple Classes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
The Joint Graphical Lasso is a generalized method for estimating Gaussian
graphical models/ sparse inverse covariance matrices/ biological networks
on multiple classes of data.  We solve JGL under two penalty functions:
The Fused Graphical Lasso (FGL), which employs a fused penalty to
encourage inverse covariance matrices to be similar across classes, and
the Group Graphical Lasso (GGL), which encourages similar network
structure between classes.  FGL is recommended over GGL for most
applications. Reference: Danaher P, Wang P, Witten DM. (2013)
<doi:10.1111/rssb.12033>.

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
