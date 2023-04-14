%global __brp_check_rpaths %{nil}
%global packname  AmpliconDuo
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Amplicon Data of the Same Sample toIdentify Artefacts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xtable 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xtable 

%description
Increasingly powerful techniques for high-throughput sequencing open the
possibility to comprehensively characterize microbial communities,
including rare species. However, a still unresolved issue are the
substantial error rates in the experimental process generating these
sequences. To overcome these limitations we propose an approach, where
each sample is split and the same amplification and sequencing protocol is
applied to both halves. This procedure should allow to detect likely PCR
and sequencing artifacts, and true rare species by comparison of the
results of both parts. The AmpliconDuo package, whereas amplicon duo from
here on refers to the two amplicon data sets of a split sample, is
intended to help interpret the obtained read frequency distribution across
split samples, and to filter the false positive reads.

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
