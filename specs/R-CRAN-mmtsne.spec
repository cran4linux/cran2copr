%global __brp_check_rpaths %{nil}
%global packname  mmtsne
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multiple Maps t-SNE

License:          FreeBSD | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
An implementation of multiple maps t-distributed stochastic neighbor
embedding (t-SNE). Multiple maps t-SNE is a method for projecting
high-dimensional data into several low-dimensional maps such that
non-metric space properties are better preserved than they would be by a
single map. Multiple maps t-SNE with only one map is equivalent to
standard t-SNE. When projecting onto more than one map, multiple maps
t-SNE estimates a set of latent weights that allow each point to
contribute to one or more maps depending on similarity relationships in
the original data. This implementation is a port of the original 'Matlab'
library by Laurens van der Maaten. See Van der Maaten and Hinton (2012)
<doi:10.1007/s10994-011-5273-4>. This material is based upon work
supported by the United States Air Force and Defense Advanced Research
Project Agency (DARPA) under Contract No. FA8750-17-C-0020. Any opinions,
findings and conclusions or recommendations expressed in this material are
those of the author(s) and do not necessarily reflect the views of the
United States Air Force and Defense Advanced Research Projects Agency.
Distribution Statement A: Approved for Public Release; Distribution
Unlimited.

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
