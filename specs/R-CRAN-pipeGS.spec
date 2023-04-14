%global __brp_check_rpaths %{nil}
%global packname  pipeGS
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Permutation p-Value Estimation for Gene Set Tests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
Requires:         R-parallel 

%description
Code for various permutation p-values estimation methods for gene set
test. The description of corresponding methods can be found in the
dissertation of Yu He(2016) "Efficient permutation P-value estimation for
gene set tests" <https://searchworks.stanford.edu/view/11849351>. One of
the methods also corresponds to the paper "Permutation p-value
approximation via generalized Stolarsky invariance" <arXiv:1603.02757>.

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
