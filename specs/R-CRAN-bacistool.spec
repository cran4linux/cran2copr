%global __brp_check_rpaths %{nil}
%global packname  bacistool
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Classification and Information Sharing (BaCIS) Tool forthe Design of Multi-Group Phase II Clinical Trials

License:          GNU General Public License (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
Requires:         R-CRAN-rjags 

%description
Provides the design of multi-group phase II clinical trials with binary
outcomes using the hierarchical Bayesian classification and information
sharing (BaCIS) model. Subgroups are classified into two clusters on the
basis of their outcomes mimicking the hypothesis testing framework.
Subsequently, information sharing takes place within subgroups in the same
cluster, rather than across all subgroups. This method can be applied to
the design and analysis of multi-group clinical trials with binary
outcomes. Reference: Nan Chen and J. Jack Lee (2019)
<doi:10.1002/bimj.201700275>.

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
%{rlibdir}/%{packname}
