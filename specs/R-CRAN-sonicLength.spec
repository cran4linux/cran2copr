%global packname  sonicLength
%global packver   1.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.6
Release:          3%{?dist}%{?buildtag}
Summary:          Estimating Abundance of Clones from DNA Fragmentation Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-splines 
Requires:         R-splines 

%description
Estimate the abundance of cell clones from the distribution of lengths of
DNA fragments (as created by sonication, whence `sonicLength').  The
algorithm in "Estimating abundances of retroviral insertion sites from DNA
fragment length data" by Berry CC, Gillet NA, Melamed A, Gormley N,
Bangham CR, Bushman FD. Bioinformatics; 2012 Mar 15;28(6):755-62 is
implemented.  The experimental setting and estimation details are
described in detail there. Briefly, integration of new DNA in a host
genome (due to retroviral infection or gene therapy) can be tracked using
DNA sequencing, potentially allowing characterization of the abundance of
individual cell clones bearing distinct integration sites. The locations
of integration sites can be determined by fragmenting the host DNA (via
sonication or fragmentase), breaking the newly integrated DNA at a known
sequence, amplifying the fragments containing both host and integrated
DNA, sequencing those amplicons, then mapping the host sequences to
positions on the reference genome. The relative number of fragments
containing a given position in the host genome estimates the relative
abundance of cells hosting the corresponding integration site, but that
number is not available and the count of amplicons per fragment varies
widely.  However, the expected number of distinct fragment lengths is a
function of the abundance of cells hosting an integration site at a given
position and a certain nuisance parameter. The algorithm implicitly
estimates that function to estimate the relative abundance.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
