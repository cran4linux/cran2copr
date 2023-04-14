%global __brp_check_rpaths %{nil}
%global packname  ace2fastq
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          3%{?dist}%{?buildtag}
Summary:          ACE File to FASTQ Converter

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringr 

%description
The ACE file format is used in genomics to store contigs from sequencing
machines. This tools converts it into FASTQ format. Both formats contain
the sequence characters and their corresponding quality information.
Unlike the FASTQ file, the ace file stores the quality values numerically.
The conversion algorithm uses the standard Sanger formula. The package
facilitates insertion into pipelines, and content inspection.

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
